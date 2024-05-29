document.getElementById('calculate-btn').addEventListener('click', function(event) {
    var compulsoryFormData = new FormData(document.getElementById('compulsory-form'));
    var optionalFormData = new FormData(document.getElementById('optional-form'));

    var compulsoryData = {};
    compulsoryFormData.forEach(function(value, key) {
        compulsoryData[key] = value;
    });

    var optionalData = {};
    optionalFormData.forEach(function(value, key) {
        optionalData[key] = value;
    });

    var data = { 'compulsory': compulsoryData, 'optional': optionalData };

    fetch('/calculate-aggregate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.total_aggregate;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
