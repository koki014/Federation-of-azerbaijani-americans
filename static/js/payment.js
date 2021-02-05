form = document.querySelector("#payment-form");
form_butt = document.querySelector("#payment-form").nextElementSibling;
console.log(form_butt);
console.log(form);

form_butt.addEventListener('click', function(){
    form.submit()
    console.log("girdim");
})