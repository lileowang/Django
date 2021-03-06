// alert('start');
console.log('start');

document.addEventListener('DOMContentLoaded', function() {
    console.log('loaded');

    document.querySelector('#submit').disabled = true;

    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
    };

    document.querySelector('form').onsubmit = () => {
        let task = document.querySelector('#task').value;
        console.log(task);

        const li = document.createElement('li');
        li.innerHTML = task;
        document.querySelector('#tasks').append(li);

        document.querySelector('#task').value = '';

        return false;
    };
});