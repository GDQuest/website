/**
 * @class SearchEngine
 * @see {@link https://gist.github.com/eddiewebb/735feb48f50f0ddd65ae5606a1cb41ae}
 * @external fuse.js
 * @external mark.js
 * @author Levrault
 */
class SearchEngine {
  searchInput = null;
  resultsField = null;
  resultsTemplate = null;
  fuse = null;
  searchQuery = "";
  summaryInclude = 60;
  minQueryLength = 2;
  maxResults = 20;
  fuseOptions = {
    shouldSort: true,
    includeMatches: true,
    threshold: 0.0,
    tokenize: true,
    location: 0,
    distance: 100,
    maxPatternLength: 32,
    minMatchCharLength: 2,
    keys: [
      {name: "title", weight: 0.8},
      {name: "keywords", weight: 0.3},
      {name: "category", weight: 0.5},
      {name: "type", weight: 0.6},
      {name: "description", weight: 0.3},
      {name: "content", weight: 0.5},
      {name: "uri", weight: 0.2},
    ],
  };

  /**
   * Decode uri to get the search's query string
   * @param {string} name - query string
   * @returns {string}
   */
  static param(name) {
    return decodeURIComponent(
      (location.search.split(name + "=")[1] || "").split("&")[0]
    ).replace(/\+/g, " ");
  }

  /**
   * @constructor
   * @param {node}    searchInput
   * @param {node}    searchContainers
   * @param {node}    resultsTemplate
   * @param {object}  [fuseOptions]
   * @param {number}  [summaryInclude]
   */
  constructor({
    searchInput,
    resultsField,
    resultsTemplate,
    url,
    fuseOptions,
    summaryInclude,
  }) {
    this.searchInput = searchInput;

    // live search
    this.searchInput.onkeyup = (e) => {
      if (this.fuse === null) return;
      this.searchQuery = e.target.value;

      var queryParams = new URLSearchParams(window.location.search);
      queryParams.set("s", e.target.value);
      history.replaceState(null, null, "?" + queryParams.toString());

      if (this.searchQuery.length >= this.minQueryLength) {
        this.executeSearch(e.target.value);
      }
    };

    this.resultsField = resultsField;
    this.resultsTemplate = resultsTemplate;
    this.url = url;
    if (fuseOptions) {
      this.fuseOptions = fuseOptions;
    }

    if (summaryInclude) {
      this.summaryInclude = summaryInclude;
    }

    this.searchQuery = this.constructor.param("s");
    this.searchInput.value = this.searchQuery;

    this.fetchArticles();
  }

  /**
   * Cache search index file
   */
  fetchArticles = () => {
    const Http = new XMLHttpRequest();
    Http.open("GET", this.url);
    Http.send();

    Http.onreadystatechange = (e) => {
      this.fuse = new Fuse(JSON.parse(Http.response), this.fuseOptions);
      if (this.searchQuery) {
        this.executeSearch(this.searchQuery);
      }
    };
  };

  /**
   * Make a XMLHttpRequest to the hugo's generated json file (url props in constructor)
   * @param {*} searchQuery
   */
  executeSearch = (searchQuery) => {
    this.resultsField.innerHTML = "No results found.";
    if (this.searchQuery.length >= this.minQueryLength) {
      var result = this.fuse.search(searchQuery);
      if (result.length > 0) {
        this.populateResults(result);
      }
    } else {
      this.resultsField.innerHTML = `Please type at least ${this.minQueryLength} characters.`;
    }
  };

  populateResults = (result) => {
    this.resultsField.innerHTML = "";
    result.slice(0, this.maxResults).forEach((value, key) => {
      let contents = value.item.content;
      let snippet = "";
      let snippetHighlights = [];

      if (this.fuseOptions.tokenize) {
        snippetHighlights.push(this.searchQuery);
      } else {
        value.matches.forEach((matchesValue) => {
          if (matchesValue.key == "tags") {
            snippetHighlights.push(matchesValue.value);
            return;
          }

          if (matchesValue.key != "content") {
            return;
          }

          let start =
            matchesValue.indices[0][0] - this.summaryInclude > 0
              ? matchesValue.indices[0][0] - this.summaryInclude
              : 0;
          let end =
            matchesValue.indices[0][1] + this.summaryInclude < contents.length
              ? matchesValue.indices[0][1] + this.summaryInclude
              : contents.length;
          snippet += contents.substring(start, end);
          snippetHighlights.push(
            matchesValue.value.substring(
              matchesValue.indices[0][0],
              matchesValue.indices[0][1] - matchesValue.indices[0][0] + 1
            )
          );
        });
      }

      if (snippet.length < 1) {
        snippet += contents.substring(0, this.summaryInclude * 2);
      }

      // pull template from hugo template definition
      let templateDefinition = this.resultsTemplate.innerHTML;
      // replace values
      let output = this.render(templateDefinition, {
        key: key,
        title: value.item.title,
        link: value.item.uri,
        snippet: snippet,
        category: value.item.category,
        difficulty: value.item.difficulty,
        type: value.item.type,
        pillClass: value.item.pillClass,
      });
      this.resultsField.innerHTML += output;

      snippetHighlights.forEach((keyword) => {
        let markTitleInstance = new Mark(document.querySelector(`#summary-${key}`));
        markTitleInstance.unmark({
          done: function () {
            markTitleInstance.mark(keyword, {exclude: ["span"]});
          },
        });
      });
    });
  };

  /**
   * Use search-result-template to format result display
   * @param {string} templateString
   * @param {object} data
   * @returns {string}
   */
  render = (templateString, data) => {
    let conditionalMatches = null;
    let conditionalPattern = /\$\{\s*isset ([a-zA-Z]*) \s*\}(.*)\$\{\s*end\s*}/g;
    let copy = templateString;

    // since loop below depends on re.lastIndex, we use a copy to capture any manipulations whilst inside the loop
    while (
      (conditionalMatches = conditionalPattern.exec(templateString)) !== null
    ) {
      if (data[conditionalMatches[1]]) {
        //valid key, remove conditionals, leave contents.
        copy = copy.replace(conditionalMatches[0], conditionalMatches[2]);
      } else {
        //not valid, remove entire section
        copy = copy.replace(conditionalMatches[0], "");
      }
    }
    templateString = copy;
    //now any conditionals removed we can do simple substitution
    var key, find, re;
    for (key in data) {
      find = "\\$\\{\\s*" + key + "\\s*\\}";
      re = new RegExp(find, "g");
      templateString = templateString.replace(re, data[key]);
    }
    return templateString;
  };
}
