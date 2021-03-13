// Loads the thumbnail of a youtube video as a placeholder to increase initial page load speed,
// especially if there are many videos on the page.
function populateVideosYoutube() {
  var youtubeVideos = document.getElementsByClassName("video-youtube");

  for (var i = 0; i < youtubeVideos.length; i++) {
    // Load the image asynchronously
    var imageSource =
      "https://i.ytimg.com/vi/" +
      youtubeVideos[i].dataset.embed +
      "/sddefault.jpg";
    var image = new Image();
    image.src = imageSource;
    image.addEventListener(
      "load",
      (function () {
        youtubeVideos[i].appendChild(image);
      })(i)
    );

    // Replace div with iframe on click
    youtubeVideos[i].addEventListener("click", function () {
      var iframe = document.createElement("iframe");

      iframe.setAttribute("frameborder", "0");
      iframe.setAttribute("allowfullscreen", "");
      iframe.setAttribute("allow", "autoplay; encrypted-media");
      iframe.setAttribute(
        "src",
        "https://www.youtube.com/embed/" + this.dataset.embed + "?autoplay=1"
      );
      this.innerHTML = "";
      this.appendChild(iframe);
    });
  }
}
