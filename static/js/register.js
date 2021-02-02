var currentTab = 0; // Current tab is set to be the first tab (0)

showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //... and fix the Next buttons:
  y = document.getElementsByClassName("form-elements");
  console.log(y);
  if (n == (x.length - 2)) {
    for (let i = 0; i < y.length; i++) {
      console.log(y[i].value);
      if(y[i].value === "") {
        console.log("qaqa nagafbgfbgfnbngfyrsan");

          document.querySelector("#nextBtn").addEventListener('click', ()=> {
            document.getElementById("nextId").innerHTML = `<button type="button" id="nextBtn" onclick="nextPrev(1)">Next</button>`;
            })
      }
      document.querySelector("#nextBtn").addEventListener('click', ()=> {
        document.getElementById("nextId").innerHTML = `<input class="submit_btn" type="submit">`;
        })
        
    }


    
  

    // element = document.getElementById("nextBtn")
    // element.setAttribute("type", "submit")
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  y = document.getElementsByClassName("form-elements");

  console.log('x', x);
  console.log('y', y);
  console.log('current', y);

  // for(let i=0; i < y.length; i++) {
  //   console.log(y[i]);
  //   if(y[i].value != "") {
      currentTab = currentTab + n;

  //   }
  // }
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByClassName("form-elements");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      document.querySelector("#nextBtn").addEventListener('click', ()=> {
        document.getElementById("nextId").innerHTML = `<button type="button" id="nextBtn" onclick="nextPrev(1)">Next</button>`;
        })

      // and set the current valid status to false
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
    document.querySelector("#nextBtn").addEventListener('click', ()=> {
      document.getElementById("nextId").innerHTML = `<input class="submit_btn" type="submit">`;
      })
  }
  return valid; // return the valid status
}
function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}