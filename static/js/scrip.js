const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');  
const goback = document.getElementById('go_back');
// click=> add|remove   

registerBtn.addEventListener('click', () =>{ 
  container.classList.add("active");
});
loginBtn.addEventListener('click', () =>{ 
  container.classList.remove("active");
}); 

// const btnShowPass = document.querySelector("#show-pass");
// const inputPass = document.querySelector("#input-pass");
// btnShowPass.addEventListener('click', function(){
//     btnShowPass.classList.toggle("active");
//     if(inputPass.type === "password"){
//         inputPass.type = "text";
//     }else {
//         inputPass.type = "password";
//     }
// });