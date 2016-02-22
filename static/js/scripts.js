/**
 * scripts.js
 *
 * Computer Science 50
 * Yale IMs
 *
 * Global JavaScript
 */

// define the number of days base on the month
function defineDays() {
    var month = Number(document.getElementById("month").value);
    
    var HTML = "";
    
    if(month == 4 || month == 6 || month == 9 || month == 11) {
        for(var i = 1; i <= 30; i++) {
            HTML += "<option value=" + i + ">" + i + "</option>";
        }
    }
    else if(month == 2) {
        for(var i = 1; i <= 28; i++) {
            HTML += ("<option value=" + i + ">" + i + "</option>");
        }
    }
    else {
        for(var i = 1; i <= 31; i++) {
           HTML += ("<option value=" + i + ">" + i + "</option>");
        }
    }
    
    document.getElementById("day").innerHTML = HTML;
}


// check if the user's inputs for the new registration were correct
function verify_submit() {
   var full_name = document.getElementById("full_name");
   var username = document.getElementById("username");
   var password = document.getElementById("password");
   var confirm_password = document.getElementById("confirm_password");
   var college = document.getElementById("college_register");
   var register_submit = document.getElementById("register_form");
   
   
   register_submit.onsubmit = function() {
      if(full_name.value == "") {
         alert("Please provide your full name");
         return false;
      }
      else if(username.value == "") {
         alert("Please provide a username");
         return false;
      }
      else if(college.value == "INVALID") {
         alert("Please select a residential college");
         return false;
      }
      else if(password.value == "") {
         alert("Please input a valid password");
         return false;
      }
      else if (confirm_password.value != password.value){
         alert("Password and confirmation don't match");
         return false;
      }
      
      return true;
   }
  
   
}

// confirm the data inputed by the user
function dataCheck() {
    
    var submit = document.getElementById("input_form");

    submit.onsubmit = function() {
        
        var sport = document.getElementById("sport");
        var strUser = sport.options[sport.selectedIndex].text;
        var month = document.getElementById("month").value;
        var day = document.getElementById("day").value;
        var year = document.getElementById("year").value;
        var college = [];
        var scores = [];
    
        if(strUser != "" && month != "" && day != "" && year != "") {
            for(var i = 1; i <= 12; i++){
                college.push(document.getElementById("cl" + i).alt);
                scores.push(document.getElementById("college" + i).value);
            }
            console.log(college);
            console.log(scores);
            
            var string = "";
            
            for(var j = 0; j < 12; j++) {
                if(scores[j] != '') {
                    string += college[j] + " " + scores[j] + "\n";    
                }
            }
            
            var answ = confirm("Your input was:" + "\n\n" + strUser + "\n" + month + "/" + day + "/" + year + "\n" + string + "\n" + "If that is correct, press 'OK'. If not, press 'Cancel'.");
        
            if(answ == true){
                return true;
            }
            else {
                return false;
            }
        }
        else {
            alert("You must provide a valid input!");
            return false;
        }
    }
}

// confirm the removal of a user
function userCheck(link) {
    var user = link.innerHTML;
    
    var ans = confirm("Press \"OK\" to remove \"" + user + "\" from the database");
    
    if(ans == true) {
        return true;
    }
    else {
        return false;
    }
}

// confirm the removal of the scores of a match
function removeScoresCheck(link) {
    var scores = link.innerHTML;
    
    var ans = confirm("Press \"OK\" to remove \"" + scores + "\" from the database");
    
    if(ans == true) {
        return true;
    }
    else {
        return false;
    }
}
