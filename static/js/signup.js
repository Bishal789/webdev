function signup(){
	let info= document.getElementsByTagName("form")[0];
	let mesg = document.getElementsByClassName("msg");
	let fname = info[0].value;
	let lname = info[1].value;
	let email = info[2].value;
	let dob = info[3].value;
	let country = info[4].value;
	let pass = info[5]. value;
	let vpass = info[6].value;

		if( fname ===""){
			mesg[0].innerHTML="First Name is Empty*"
			return false;
		}
		if( lname ===""){
			mesg[1].innerHTML="Last Name is Empty*"
			return false;
		}
		if( email ===""){
			mesg[2].innerHTML="Email is Empty*"
			return false;
		}
		
		if( dob ===""){
			mesg[3].innerHTML="Date of Birth is Empty*"
			return false;
		}
		if( country ===""){
			mesg[4].innerHTML="Country is Empty*"
			return false;
		}
		if (pass ===""){
			mesg[5].innerHTML="Password Needed*"
			return false;
		}if ( vpass ===""){
			mesg[6].innerHTML="Password Needed*"
			return false;
		}
		if ( pass != vpass){
			mesg[6].innerHTML="Password doesn't Match*"
			return false;
		}
		








	return true;
}
