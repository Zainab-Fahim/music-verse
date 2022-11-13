import wixWindow from 'wix-window';
import {fetch} from 'wix-fetch';
$w.onReady(function () {

});

/**
*	Adds an event handler that runs when the element is clicked.
	[Read more](https://www.wix.com/corvid/reference/$w.ClickableMixin.html#onClick)
*	 @param {$w.MouseEvent} event
*/

/**
*	Adds an event handler that runs when the element is clicked.
	[Read more](https://www.wix.com/corvid/reference/$w.ClickableMixin.html#onClick)
*	 @param {$w.MouseEvent} event
*/
export function sendButton_click_1(event) {
	// This function was added from the Properties & Events panel. To learn more, visit http://wix.to/UcBnC-4
	// Add your code for this event here: 
		wixWindow.getCurrentGeolocation()
    .then( (obj) => {
		console.log("IN FUNCT");
        let latitude = obj.coords.latitude;             // 32.0971036
        let longitude = obj.coords.longitude;           // 34.774391099999995          
		console.log(latitude);
		let phoneNum = $w('#phoneNumber').value;
		//https://med-circle-1873.twil.io/nearest-music-store
		//https://music-verse-3898.twil.io/nearest-music-store
		//https://music-verse-3898.twil.io/nearest-music-store
		fetch(`https://music-verse-3898.twil.io/nearest-music-store?receipent_contact=whatsapp:%2B91${phoneNum}&latitude=${latitude}&longitude=${longitude}`, {"method": "get"})
			.then( (httpResponse) => {
				if (httpResponse.ok) {
				return httpResponse.json();
				} else {
				return Promise.reject("Fetch did not succeed");
				}
			} )
			.then(json => console.log(json.someKey))
			.catch(err => console.log("CATCH ERROR IS: ",err));
		})
    .catch( (error) => {
        let errorMsg = error;
    });
}
