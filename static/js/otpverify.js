function OTP_verify(){
    
    reg_otp_option = document.getElementById("OTP-option").value

    reg_phone = document.getElementById("reg_phone").value

    reg_email = document.getElementById("reg_email_id").value

    if(reg_otp_option == ""){
        alert("Please select Option..!")
        return false;
    }
    alert("Option is "+reg_otp_option);
    if(reg_phone == ""){
        alert("Please Enter Number");
        return false;

    }
    else if(reg_email == ""){
        alert("Please Enter Email");
        return false;
    }

    if(reg_otp_option == "Phone"){
        window.location.href = "OTP_verify/" + reg_phone;
        alert("OTP Has Been send to your phone ")

        return true;


    }
    else if(reg_otp_option == "Email"){
        window.location.href = "OTP_verify/" + reg_email;
        alert("OTP Has Been send to your gmail ")

        return true
    }
    
    

    
}