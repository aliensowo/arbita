export default class QuantityField {
	
	constructor() {
		this.quantitySubBtns = document.querySelectorAll('.quantity-sub');
		this.quantityAddBtns = document.querySelectorAll('.quantity-add');
		
		if(this.quantitySubBtns){
			this.listenerSub(this.quantitySubBtns)
		}
		
		if(this.quantityAddBtns){
			this.listenerAdd(this.quantityAddBtns)
		}
	}
	
	listenerSub (quantitySubBtns) {
	
		Array.from(quantitySubBtns).map((index)=>{
			index.addEventListener('click', ()=> {
				const quantityField = index.closest('.quantity-block_item').querySelector('.quantity-field');
				const quantityFieldValue = quantityField.getAttribute('value');
				
				if(quantityFieldValue > 1) {
					quantityField.setAttribute('value', Number(quantityFieldValue) - 1);
				}
			})
		})
	}
	
	listenerAdd (quantityAddBtns) {
		
		Array.from(quantityAddBtns).map((index)=>{
			index.addEventListener('click', ()=> {
				const quantityField = index.closest('.quantity-block_item').querySelector('.quantity-field');
				const quantityFieldValue = quantityField.getAttribute('value');
				
				quantityField.setAttribute('value', Number(quantityFieldValue) + 1);
			})
		})
	}
}