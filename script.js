document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('expansionForm');
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const n = document.querySelector('#n').value;
        
        if (n < 0) {
            document.querySelector('#result').innerHTML = '<p>Please enter a non-negative integer.</p>';
            return;
        }

        document.querySelector('#loading').style.display = 'block';
        document.querySelector('#result').innerHTML = '';

        try {
            const response = await fetch(`http://localhost:8080/expansion?n=${n}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            let result = await response.text();


            result = result.replace(/\^(\d+)/g, '<sup>$1</sup>');

            document.querySelector('#result').innerHTML = `<p>${result}</p>`;
        } catch (error) {
            document.querySelector('#result').innerHTML = `<p>Error: ${error.message}</p>`;
        } finally {
            document.querySelector('#loading').style.display = 'none';
        }
    });
});
