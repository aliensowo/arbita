export default class Modal {
	
	constructor() {
		this.doc = document;
		this.modalLinks = this.doc.querySelectorAll('.modal-link');
		this.modals = this.doc.querySelectorAll('.modal');
		this.modalCloseLinks = this.doc.querySelectorAll('.modal_close');
		
		if(this.modalLinks && this.modals) {
			this.listener(this.modalLinks, this.modals, this.modalCloseLinks);
		}
	}
	
	listener(modalLinks, modals, modalCloseLinks = undefined) {
		
		for(let link of modalLinks) {
			link.addEventListener('click', ()=> {
				let modalId = link.getAttribute('data-modal');
				
				this.openModal(modalId);
			})
		}
		
		for(let modal of modals) {
			modal.addEventListener('click', (e)=> {
				
				if(e.target === e.currentTarget) {
					this.closeModals();
				}
			})
		}
		
		if(modalCloseLinks) {
			
			for(let close of modalCloseLinks) {
				close.addEventListener('click', ()=> {
					this.closeModals();
				})
			}
		}
	}
	
	openModal (modalId) {
		const modal = document.getElementById(modalId);
		
		this.closeModals();
		modal.classList.add('is-open');
	}
	
	closeModals () {
		
		for(let modal of this.modals) {
			modal.classList.remove('is-open');
		}
	}
}