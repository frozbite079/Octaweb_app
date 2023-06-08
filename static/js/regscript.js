function regfunc(){
    //html field ID
    
    reg_name = document.getElementById("reg_name").value

    reg_phone = document.getElementById("reg_phone").value

    reg_email = document.getElementById("reg_email_id").value

    reg_pass = document.getElementById("reg_pass").value

    reg_pass_re = document.getElementById("reg_repass").value
    
    reg_otp = document.getElementById("reg_otp").value

    //const email = reg_email;
    //const pattern = /@gmail.com/;
    //const result = email.test(pattern)

    if(reg_name == ""){
        alert("Please Enter UserName")
        return false;
    }
    else if(reg_phone == ""){
        alert("Please Enter Phone Number")
        return false;
    } 
    else if(reg_email == ""){
        alert("Please Enter Email")
        return false;
    }
   // else if(result == false){
       // alert("Please Enter valid Gmail")
        //return false;
   // }
    else if(reg_pass == ""){
        alert("Please Enter Password")
        return false;
    }
    else if(reg_pass_re == ""){
        alert("PLease Enter Repeat Password")
        return false;
    }
    else if(reg_otp == ""){
        alert("Please Enter OTP");
        return false;
    }

    if(reg_pass_re != reg_pass){
        alert("Both Password should be same")
        return false;

    }
    
    //alert("ok");

    window.location.href = "get_data/"+reg_name+"/"+reg_otp;
    return false; 
    

}