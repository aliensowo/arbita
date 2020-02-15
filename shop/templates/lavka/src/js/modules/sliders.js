import { tns } from "tiny-slider/src/tiny-slider"

export default class Sliders {
	
	constructor() {
		const serviceSliders = document.querySelectorAll('.services-slider_inner');
		const successSliders = document.querySelectorAll('.success-slider_slider');
		
		if(serviceSliders) {
			
			Array.from(serviceSliders).map((index)=> {
				return tns({
						container: index,
						mode: 'gallery',
						items: 1,
						mouseDrag: true,
						loop: true,
						nav: true,
						swipeAngle: false,
						speed: 400,
						controlsText: ['', ''],
					});
			})
		}
		
		if(successSliders){
			
			Array.from(successSliders).map((index)=> {
				return tns({
					container: index,
					items: 2,
					mouseDrag: true,
					loop: true,
					nav: false,
					gutter: 20,
					swipeAngle: false,
					speed: 400,
					controlsText: ['', ''],
					responsive: {
						769: {
							items: 2,
							gutter: 20,
						},
						320: {
							items: 1,
							gutter: 0
						}
					}
				});
			})
		}
	}
}