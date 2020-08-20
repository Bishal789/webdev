function validation(){
	let abc = document.getElementsByTagName("form")[0];
	let error= document.getElementsByClassName('error');
	let userid = abc[0].value;
	let password = abc[1].value;
		if (userid === ""  ){
			error[0].innerHTML= " *Please Fill you Email/Phone";
			return false;
		}
		if (password === "" ){
			error[1].innerHTML= " *Please Fill you Password";
			return false;
		}

		
	
	return true;
	}
