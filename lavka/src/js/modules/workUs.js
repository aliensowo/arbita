export default class WorkUs {
	constructor() {
		const workUsBlock = document.querySelector('.work-us');
		
		if(workUsBlock) {
			const workUsLink = workUsBlock.querySelector('.work-us_title');
			
			workUsLink.addEventListener('click', ()=> {
				workUsBlock.classList.toggle('is-show');
			});
			
			workUsBlock.addEventListener('mouseleave', ()=> {
				workUsBlock.classList.remove('is-show');
			});
		}
	}
}