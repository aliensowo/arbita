export default class Order {
	
	constructor() {
	    this.modalOrders = document.querySelectorAll('.modal-order');
	    
	    Array.from(this.modalOrders).map((modal) => {
	    	this.handlerOrder(modal)
	    });
	}
	
	handlerOrder(modal) {
		
		const modalCurrent = modal;
		const buyBtns = Array.from(modal.querySelectorAll('.order-product_btn'));
		
		this.handlerSteps(modalCurrent);
		
		buyBtns.map((btn) => {
			btn.addEventListener('click', ()=>{
				this.handlerBtn(btn);
			})
		})
	}
	
	handlerSteps(modal, step = 1) {
		const steps = modal.querySelector('.modal_steps');
		const orderSteps = Array.from(modal.querySelectorAll('.order-step'));
		
		if(steps) {
			const stepNumber = steps.querySelector('.modal_steps__number');
			const stepValues = Array.from(steps.querySelectorAll('.modal_steps__items-value'));
			
			stepNumber.textContent = step;
			
			stepValues.map((index) => {
				
				if(Number(index.getAttribute('data-order-step')) <= step) {
					index.classList.add('is-active');
				}
			})
		}
		
		if(orderSteps) {
			
			orderSteps.map((index) => {
				const orderStep  = Number(index.getAttribute('data-order-step'));
				
				if(orderStep === step) {
					index.classList.add('is-active');
				} else {
					index.classList.remove('is-active');
				}
			})
		}
	}
	
	handlerBtn(btn) {
		const stepNumber = Number(btn.closest('.order-step').getAttribute('data-order-step'));
		const modal = btn.closest('.modal-order');
		this.handlerSteps(modal, stepNumber + 1);
	}
}