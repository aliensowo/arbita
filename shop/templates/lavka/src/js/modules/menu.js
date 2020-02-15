export default class Menu {
	
	constructor() {
		const submenus = Array.from(document.querySelectorAll('.submenu'));
		
		if(submenus) {
			const header = document.querySelector('.site_header');
			
			if(document.body.clientWidth > 992) {
				
				this.handlerDesktop(header, submenus);
				
			} else {
				
				this.handlerMobile(header, submenus);
			}
		}
	}
	
	handlerDesktop(header, submenus) {
		submenus.map((submenu) => {
			const submenuLink = submenu.querySelector('.nav_item__link');
			
			submenuLink.addEventListener('mouseenter', ()=> {
				
				const submenuItems = Array.from(document.querySelectorAll('.nav_item.submenu'));
				
				submenuItems.map((submenuItem) => {
					submenuItem.classList.remove('is-active');
				});
				
				submenu.classList.add('is-active');
				header.classList.add('is-open-menu');
			})
		});
		
		header.addEventListener('mouseleave', ()=> {
			header.classList.remove('is-open-menu');
			
			submenus.map((submenu) => {
				submenu.classList.remove('is-active');
			})
		})
	}
	
	handlerMobile(header, submenus) {
		const menuBtn = document.getElementById('menu-toggle');
		const html = document.querySelector('html');
		
		if(menuBtn) {
			
			menuBtn.addEventListener('click', ()=> {
				
				if(header.classList.contains('is-open-menu')) {
					const submenuItems = Array.from(document.querySelectorAll('.nav_item.submenu'));
					
					header.classList.remove('is-open-menu');
					
					if(document.body.clientWidth < 576) {
						html.classList.remove('is-trimmed');
					}
					
					submenuItems.map((submenuItem) => {
						submenuItem.classList.remove('is-active');
					});
				} else {
					header.classList.add('is-open-menu');
					
					if(document.body.clientWidth < 576) {
						html.classList.add('is-trimmed');
					}
				}
			})
		}
		
		submenus.map((submenu) => {
			const submenuLink = submenu.querySelector('.nav_item__link');
			
			submenuLink.addEventListener('click', ()=> {
				
				const submenuItems = Array.from(document.querySelectorAll('.nav_item.submenu'));
				
				submenuItems.map((submenuItem) => {
					submenuItem.classList.remove('is-active');
				});
				
				submenu.classList.add('is-active');
			})
		});
	}
}