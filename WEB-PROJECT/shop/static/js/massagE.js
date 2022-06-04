function checkFirst() {
    var first = document.getElementById("first").value;
    var regex = /^[a-zA-Z\s]{2,15}$/;
  
    if (regex.test(first)) { // if testing of first is true
        document.getElementById("first_Check").style.color = "green";
        document.getElementById("first_Check").innerHTML = "Input correct :)";
        return true;
    }
    else {// if it's not
        document.getElementById("first_Check").style.color = "red";
        document.getElementById("first_Check").innerHTML = "Please, enter 2-15 characters";
        return false;
    }
  }
  //Checking of email field
  function checkEmail() {
    var email = document.getElementById("email").value;
    var regex = /^[0-9a-zA-Z_.-]+[@][0-9a-zA-Z_.-]+([.][a-zA-Z]+){1,2}$/;
  
    if (regex.test(email)) { // if testing of first is true
        document.getElementById("email_Check").style.color = "green";
        document.getElementById("email_Check").innerHTML = "Email correct :)";
        return true;
    }
    else {// if it's not
        document.getElementById("email_Check").style.color = "red";
        document.getElementById("email_Check").innerHTML = "Email is incorrect!";
        return false;
    }
  }
  //Checking of Phone number field
  function checkPhone() {
    var phone = document.getElementById("phone").value;
    var regex = /^8[3|4|9|7|8]\d{9}$/;
  
    if (regex.test(phone)) { // if testing of first is true
        document.getElementById("phone_Check").style.color = "green";
        document.getElementById("phone_Check").innerHTML = "Input correct :)";
        return true;
    }
    else {// if it's not
        document.getElementById("phone_Check").style.color = "red";
        document.getElementById("phone_Check").innerHTML = "Input is incorrect!";
        return false;
    }
  }

    
  //Collect and output all the data
  function outputData() {
    var first = document.getElementById("first").value;
    var last = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
  
  
    if (first != "" && email != ""  && phone != "" ) {
        document.getElementById("summary").style.color = "black";
        document.getElementById("summary").innerHTML = "Hello, " + first + " " + last + "!";
        document.getElementById("summary").innerHTML += "<p>Your order was successfully placed. We will contact you as soon as possible. You can see the details of your order below: </p>";
        document.getElementById("summary").innerHTML += "<p>Phone number: " + phone + ".</br>";
        document.getElementById("summary").innerHTML += "Email: " + email + ".</br>";
        document.getElementById("summary").innerHTML += "<p style='font-weight: bold;'>We are glad that You use our company's services :)</p>";
    }
    else {
        document.getElementById("summary").style.color="red";
        document.getElementById("summary").innerHTML = "Please, fill in all the fields...";
    }
  }
  