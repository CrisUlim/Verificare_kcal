// Function to delete a row from the table
function deleteRow(button, foodName) {
    const row = button.closest('tr');
    row.remove();
    updateTotals();
    updateProgressBar();

    // Optional: Send request to the server to update session
    fetch('/remove-food/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify({
            food_name: foodName
        })
    }).then(response => {
        if (response.ok) {
            console.log(`${foodName} removed.`);
        } else {
            console.error('Failed to remove food from the session.');
        }
    }).catch(error => console.error('Error:', error));
}

// Function to update totals in the footer
function updateTotals() {
    let totalCarbs = 0,
        totalProtein = 0,
        totalFats = 0,
        totalCalories = 0;

    document.querySelectorAll('#table tbody tr').forEach(row => {
        totalCarbs += parseFloat(row.cells[1].textContent || 0);
        totalProtein += parseFloat(row.cells[2].textContent || 0);
        totalFats += parseFloat(row.cells[3].textContent || 0);
        totalCalories += parseFloat(row.cells[4].textContent || 0);
    });

    document.getElementById('totalCarbs').textContent = totalCarbs.toFixed(2);
    document.getElementById('totalProtien').textContent = totalProtein.toFixed(2);
    document.getElementById('totalFats').textContent = totalFats.toFixed(2);
    document.getElementById('totalCalories').textContent = totalCalories.toFixed(2);
}

// Function to update the progress bar
function updateProgressBar() {
    const calorieGoal = {
        {
            calorie_goal
        }
    };
    let totalCalories = parseFloat(document.getElementById('totalCalories').textContent || 0);
    const percentage = Math.min((totalCalories / calorieGoal) * 100, 100).toFixed(2);

    const progressBar = document.getElementById('calorieProgressBar');
    const progressText = document.getElementById('calorieProgressText');

    progressBar.style.width = `${percentage}%`;
    progressBar.setAttribute('aria-valuenow', percentage);
    progressText.textContent = `${totalCalories.toFixed(2)} / ${calorieGoal} Kcal`;

    // Change color based on percentage
    if (percentage < 50) {
        progressBar.classList.remove('bg-warning', 'bg-danger');
        progressBar.classList.add('bg-success');
    } else if (percentage < 90) {
        progressBar.classList.remove('bg-success', 'bg-danger');
        progressBar.classList.add('bg-warning');
    } else {
        progressBar.classList.remove('bg-success', 'bg-warning');
        progressBar.classList.add('bg-danger');
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateTotals();
    updateProgressBar();
});

// Helper function to get CSRF token
function getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}