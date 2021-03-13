// Use lazy loading for autoplaying <video>.
// This is not required for Chrome as it performs lazy loading for such videos
// automatically, but other browsers like Firefox don't do this yet.
function lazyLoadVideos() {
  const lazyVideos = [].slice.call(
    document.querySelectorAll("video[data-lazy]")
  );
  if ("IntersectionObserver" in window) {
    const lazyVideoObserver = new IntersectionObserver(function (
      entries,
      observer
    ) {
      entries.forEach(function (video) {
        if (video.isIntersecting) {
          for (let source in video.target.children) {
            const videoSource = video.target.children[source];
            if (
              typeof videoSource.tagName === "string" &&
              videoSource.tagName === "SOURCE"
            ) {
              videoSource.src = videoSource.dataset.src;
            }
          }

          video.target.load();
          lazyVideoObserver.unobserve(video.target);
        }
      });
    });

    lazyVideos.forEach(function (lazyVideo) {
      lazyVideoObserver.observe(lazyVideo);
    });
  }
}

document.addEventListener("DOMContentLoaded", lazyLoadVideos);
