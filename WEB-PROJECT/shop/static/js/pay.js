//Checking of Fisrt name field
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
  
  
  //Checking of Last name field
  function checkLast() {
    var last = document.getElementById("last").value;
    var regex = /^[a-zA-Z\s]{2,20}$/;
  
    if (regex.test(last)) { // if testing of first is true
        document.getElementById("last_Check").style.color = "green";
        document.getElementById("last_Check").innerHTML = "Input correct :)";
        return true;
    }
    else {// if it's not
        document.getElementById("last_Check").style.color = "red";
        document.getElementById("last_Check").innerHTML = "Please, enter 2-20 characters";
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
    //Checking of cerd number field
    function checkDest() {
        var dest = document.getElementById("dest").value;
        var regex = /^\d{16}|\d{19}$/;
      
        if (regex.test(dest)) { // if testing of dest is true
            document.getElementById("dest_Check").style.color = "green";
            document.getElementById("dest_Check").innerHTML = "Input correct :)";
            return true;
        }
        else {// if it's not
            document.getElementById("dest_Check").style.color = "red";
            document.getElementById("dest_Check").innerHTML = "Please, enter 16 number";
            return false;
        }
      }
       //Checking of Time limit of card field
    function checkQuantity() {
        var dest = document.getElementById("quantity").value;
        var regex = /^（0[1-9]1[0-2])-[0-9]{2}$/;
      
        if (regex.test(dest)) { // if testing of dest is true
            document.getElementById("quantity_Check").style.color = "green";
            document.getElementById("quantity_Check").innerHTML = "Input correct :)";
            return true;
        }
        else {// if it's not
            document.getElementById("quantity_Check").style.color = "red";
            document.getElementById("quantity_Check").innerHTML = "Please, enter mouth/year";
            return false;
        }
      }
      
  
  //Collect and output all the data
  function outputData() {
    var first = document.getElementById("first").value;
    var last = document.getElementById("last").value;
    var dest = document.getElementById("dest").value;
    var phone = document.getElementById("phone").value;
    var quantity = document.getElementById("quantity").value;
    var paymethod = document.getElementById("paymethod").value;
  
    if (first != "" && last != "" && dest != "" && phone != "" && quantity != "") {
        document.getElementById("summary").style.color = "black";
        document.getElementById("summary").innerHTML = "Hello, " + first + " " + last + "!";
        document.getElementById("summary").innerHTML += "<p>Your order was successfully placed. We will contact you as soon as possible. You can see the details of your order below: </p>";
        document.getElementById("summary").innerHTML += "<p>Phone number: " + phone + ".</br>";
        document.getElementById("summary").innerHTML += "Card number: " + dest + ".</br>";
        document.getElementById("summary").innerHTML += "<p>Time limit of card: " + quantity + ".</br>";
        document.getElementById("summary").innerHTML += "Bank Card: " + paymethod + ".</p>";
        document.getElementById("summary").innerHTML += "<p style='font-weight: bold;'>We are glad that You use our company's services :)</p>";
    }
    else {
        document.getElementById("summary").style.color="red";
        document.getElementById("summary").innerHTML = "Please, fill in all the fields...";
    }
  }