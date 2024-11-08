let currentTargetId = null;

function showProjectDetails(projectId) {
    // Show the project details
    document.getElementById('project').style.display = 'block';
    document.getElementById('target').style.display = 'none';
    // Fetch the project details using AJAX or fetch API
    fetch(`/project/${projectId}`)
      .then(response => response.json())
      .then(data => {
        document.getElementById('project-name').innerText = data.project.name;
        document.getElementById('project-description').innerText = data.project.description;
        document.getElementById('project-state').innerText = data.project.state;
        document.getElementById('project-priority').innerText = data.project.priority;
        document.getElementById('project-minimumtime').innerText = data.project.minimumtime;
        document.getElementById('project-minimumalt').innerText = data.project.minimumaltitude;
        document.getElementById('project-usecustomhorizon').innerText = data.project.usecustomhorizon ? 'True' : 'False';
        document.getElementById('project-horizonoffset').innerText = data.project.horizonoffset;
        document.getElementById('project-meridianwindow').innerText = data.project.meridianwindow;
        document.getElementById('project-filterswitchfrequency').innerText = data.project.filterswitchfrequency;
        document.getElementById('project-ditherevery').innerText = data.project.ditherevery;
        document.getElementById('project-enablegrader').innerText = data.project.enablegrader ? 'True' : 'False';
        document.getElementById('project-ismosaic').innerText = data.project.isMosaic ? 'True' : 'False';
        document.getElementById('project-flatshandling').innerText = data.project.flatsHandling;
      });
  }

  function showTargetDetails(targetId) {
    currentTargetId = targetId; // Set the current target ID
    // Hide the project details
    document.getElementById('project').style.display = 'none';
    document.getElementById('target').style.display = 'block';
    // Fetch the project details using AJAX or fetch API
    fetch(`/target/${targetId}`)
      .then(response => response.json())
      .then(data => {
        // Update the target details
        document.getElementById('target-name').innerText = data.target.name;
        document.getElementById('target-enabled').innerText = data.target.active ? 'True' : 'False';
        document.getElementById('target-coordinates').innerText = data.target.coordinates;
        document.getElementById('target-rotation').innerText = `${data.target.rotation}°`;
        document.getElementById('target-roi').innerText = `${data.target.roi}%`;

        exposureTemplates = data.exposureTemplates;

        // Update the exposure plans
        const exposurePlansTable = document.getElementById('exposure-plans');
        exposurePlansTable.innerHTML = '';
        data.exposurePlans.forEach(plan => {
          const template = exposureTemplates.find(t => t.Id === plan.exposureTemplateId);
          const filtername = template ? template.filtername : 'Unknown';
          const row = document.createElement('tr');
          row.innerHTML = `
            <td class="px-4 py-2">${filtername}</td>
            <td class="px-4 py-2">${plan.exposure === -1 ? '(Template)' : plan.exposure}</td>
            <td class="px-4 py-2"><input type="number" value="${plan.desired}" onchange="updateExposurePlan(${plan.Id}, 'desired', this.value)"></td>
            <td class="px-4 py-2"><input type="number" value="${plan.accepted}" onchange="updateExposurePlan(${plan.Id}, 'accepted', this.value)"></td> 
            <td class="px-4 py-2">${plan.acquired}</td>   
            <td class="px-4 py-2">${(plan.accepted / plan.desired * 100).toFixed(2)}%</td>
          `;
          exposurePlansTable.appendChild(row);
        });
      });
  }

  function updateExposurePlan(planId, field, newValue) {
    fetch(`/update-exposureplan/${planId}/${field}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ value: newValue })
    })
    .then(response => response.json())
    .then(data => {
      if (!data.success) {
        alert('Failed to update ' + field + ' value');
      }
    });
  }

  function toggleTargets(projectId) {
    const targetList = document.getElementById(`targets-${projectId}`);
    if (targetList) {
      if (targetList.style.display === 'none') {
        targetList.style.display = 'block';
      } else {
        targetList.style.display = 'none';
      }
    }
  }

  function toggleTargetEnabled() {
    const targetEnabledElement = document.getElementById('target-enabled');
    const currentStatus = targetEnabledElement.innerText === 'True';
    const newStatus = !currentStatus;

    fetch(`/toggle-target-enabled/${currentTargetId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ enabled: newStatus })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        targetEnabledElement.innerText = newStatus ? 'True' : 'False';
      } else {
        alert('Failed to update target status');
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    const resizer = document.querySelector('.resizer');
    const sidebar = document.querySelector('.sidebar');
    let isResizing = false;

    resizer.addEventListener('mousedown', function (e) {
      isResizing = true;
      document.body.style.cursor = 'ew-resize';
    });

    document.addEventListener('mousemove', function (e) {
      if (!isResizing) return;
      const newWidth = e.clientX - sidebar.getBoundingClientRect().left;
      if (newWidth >= 200 && newWidth <= 400) {
        sidebar.style.width = `${newWidth}px`;
      }
    });

    document.addEventListener('mouseup', function () {
      isResizing = false;
      document.body.style.cursor = 'default';
    });
  });