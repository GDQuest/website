class LazyLoad {
	constructor() {
		this.imgTags = document.getElementsByTagName("img");
		this.lastMaxScrollPos = 0;

		const RANGE = 200;
		const USE_FADE = true;
		const SRC_ATTRIBUTE = "data-src";

		this.imgTags = this.imgTags.filter(function (element) {
			if (USE_FADE) element.setStyle("opacity", 0);
			var elementPos = element.getPosition()["y"];
			if (elementPos < window.getSize()[axis] + RANGE) {
				this.loadImage(element);
				return false;
			}
			return true;
		}, this);

		var action = function (e) {
			var currentPos = window.getScroll()[axis];
			if (currentPos > this.lastMaxScrollPos) {
				this.imgTags = this.imgTags.filter(function (el) {
					if ((currentPos + RANGE + window.getSize()[axis]) >= el.getPosition()[axis]) {
						this.loadImage(el);
						return false;
					}
					return true;
				}, this);

				this.lastMaxScrollPos = currentPos;
			}
			this.fireEvent("scroll");

			if (!this.imgTags.length) {
				window.removeEvent("scroll", action);
				this.fireEvent("complete");
			}
		}.bind(this);

		window.addEvent("scroll", action);
	}

	loadImage(image) {
		if (USE_FADE) {
			image.addEvent("load", function () {
				image.fade(1);
			});
		}
		image.set("src", image.get(SRC_ATTRIBUTE));
		this.fireEvent("load", [image]);
	}
}

export { LazyLoad }