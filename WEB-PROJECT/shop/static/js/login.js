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
      var phone = document.getElementById("phone").value;
    
      if ( phone != "" ) {
          document.getElementById("summary").style.color = "black";
          document.getElementById("summary").innerHTML += "<p>Phone number: " + phone + ".</br>";
          document.getElementById("summary").innerHTML += "<p style='font-weight: bold;'>We are glad that You use our company's services :)</p>";
      }
      else {
          document.getElementById("summary").style.color="red";
          document.getElementById("summary").innerHTML = "Please, fill in all the fields...";
      }
    }