const GAUGE_MAXIMUMS = {
    'rpm': 5000,
    'speed': 50,
};

const MAX_ANGLES = {
    'rpm': 225,
    'speed': 225,
};

function setGaugeClusterData(data) {
    Object.entries(JSON.parse(data)).forEach(entry => {
        const [key, value] = entry;
        let angle = MAX_ANGLES[key] / GAUGE_MAXIMUMS[key] * value;
        document.getElementById(`${key}-needle`).style.setProperty('--needle-angle', `${angle}deg`);
    });
}

event_stream = new ReconnectingEventSource('event-stream/');

event_stream.addEventListener('message', function (event) {
    setGaugeClusterData(event.data);
}, false);