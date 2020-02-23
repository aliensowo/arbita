export default class Order {
	
	constructor() {
	    this.modalOrders = document.querySelectorAll('.modal-orders');
	    
	    Array.from(this.modalOrders).map((modal) => {
	    	this.handlerOrder(modal)
	    });
	}
	
	handlerOrder(modal) {
		
		const modalCurrent = modal;
		const buyBtns = Array.from(modal.querySelectorAll('.orders-product_btn'));
		
		this.handlerSteps(modalCurrent);
		
		buyBtns.map((btn) => {
			btn.addEventListener('click', ()=>{
				this.handlerBtn(btn);
			})
		})
	}
	
	handlerSteps(modal, step = 1) {
		const steps = modal.querySelector('.modal_steps');
		const orderSteps = Array.from(modal.querySelectorAll('.orders-step'));
		
		if(steps) {
			const stepNumber = steps.querySelector('.modal_steps__number');
			const stepValues = Array.from(steps.querySelectorAll('.modal_steps__items-value'));
			
			stepNumber.textContent = step;
			
			stepValues.map((index) => {
				
				if(Number(index.getAttribute('data-orders-step')) <= step) {
					index.classList.add('is-active');
				}
			})
		}
		
		if(orderSteps) {
			
			orderSteps.map((index) => {
				const orderStep  = Number(index.getAttribute('data-orders-step'));
				
				if(orderStep === step) {
					index.classList.add('is-active');
				} else {
					index.classList.remove('is-active');
				}
			})
		}
	}
	
	handlerBtn(btn) {
		const stepNumber = Number(btn.closest('.orders-step').getAttribute('data-orders-step'));
		const modal = btn.closest('.modal-orders');
		this.handlerSteps(modal, stepNumber + 1);
	}
}