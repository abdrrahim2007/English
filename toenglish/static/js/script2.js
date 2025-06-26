
const conversationsBtn = document.getElementById('conversations-btn');
const vocabularyBtn = document.getElementById('vocabulary-btn');
const storiesBtn = document.getElementById('stories-btn');
const conversationsSection = document.getElementById('conversations');
const vocabularySection = document.getElementById('vocabulary');
const storiesSection = document.getElementById('stories');

conversationsBtn.addEventListener('click', () => {
  conversationsSection.style.display = 'flex';
  vocabularySection.style.display = 'none';
  storiesSection.style.display = 'none';
});

vocabularyBtn.addEventListener('click', () => {
  conversationsSection.style.display = 'none';
  vocabularySection.style.display = 'flex';
  storiesSection.style.display = 'none';
});

storiesBtn.addEventListener('click', () => {
  conversationsSection.style.display = 'none';
  vocabularySection.style.display = 'none';
  storiesSection.style.display = 'flex';
});

addNewC = document.getElementById('add-new-c')
addIconC = document.getElementById('addIconC')
closeIconC = document.getElementById('closeIconC')
addIconC.addEventListener('click',()=>{
    addNewC.style.display='flex'
})
closeIconC.addEventListener('click',()=>{
    addNewC.style.display='none'
})

addNewV = document.getElementById('add-new-v')
addIconV = document.getElementById('addIconV')
closeIconV = document.getElementById('closeIconV')
addIconV.addEventListener('click',()=>{
    addNewV.style.display='flex'
})
closeIconV.addEventListener('click',()=>{
    addNewV.style.display='none'
})

addNewS = document.getElementById('add-new-s')
addIconS = document.getElementById('addIconS')
closeIconS = document.getElementById('closeIconS')
addIconS.addEventListener('click',()=>{
    addNewS.style.display='flex'
})
closeIconS.addEventListener('click',()=>{
    addNewS.style.display='none'
})
window.onload = function() {
      const urlParams = new URLSearchParams(window.location.search);
      const section = urlParams.get('section');

      if (section === 'stories') {
        storiesSection.style.display = 'flex';
        conversationsSection.style.display = 'none';
        vocabularySection.style.display = 'none';
        
      }
      if (section === 'vocabulary') {
        vocabularySection.style.display = 'flex';
        conversationsSection.style.display = 'none';
        storiesSection.style.display = 'none';
      }
      if (section === 'conversations') {
        conversationsSection.style.display = 'flex';
        storiesSection.style.display = 'none';
        vocabularySection.style.display = 'none';
      }
    };



// var playbtns = document.getElementsByClassName('play-icon')
// for (var i = 0; i < playbtns.length; i++) {
//     playbtns[i].addEventListener('click',function(){
//         var soundUrl = this.dataset.sound
        
//         addSoundUrl(soundUrl)
            
        
        
//     })
// }
// function addSoundUrl(soundUrl){
//     var audio = new Audio(soundUrl);
//     var isPlaying = false;
    
//     function playSound() {
//       if (isPlaying) {
//         audio.pause();
//         audio.currentTime = 0;
//       }
      
//       audio.play();
//       isPlaying = true;
//     }
// }