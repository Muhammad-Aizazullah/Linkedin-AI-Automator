// Dashboard k liye basic timer aur UI updates
function updateTimer() {
    let timerElement = document.getElementById('timer');
    if (timerElement) {
        let now = new Date();
        let target = new Date();
        target.setHours(11, 59, 0, 0);
        
        if (now > target) {
            target.setDate(target.getDate() + 1);
        }
        
        let diff = target - now;
        let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        
        timerElement.innerText = "Auto-post in " + hours + "h " + mins + "m";
    }
}
setInterval(updateTimer, 60000);
updateTimer();