const GAUGE_BOUNDS = {
    'rpm': [0, 5000],
    'speed': [0, 50],
};

const MAX_ANGLES = {
    'rpm': 225,
    'speed': 225,
};

function setGaugeClusterData(data) {
    Object.entries(JSON.parse(data)).forEach(entry => {
        const [key, value] = entry;
        let mapping_slope = MAX_ANGLES[key] / (GAUGE_BOUNDS[key][1] - GAUGE_BOUNDS[key][0]);
        let angle = mapping_slope * value - GAUGE_BOUNDS[key][0] * mapping_slope;
        document.getElementById(`${key}-needle`).style.setProperty('--needle-angle', `${angle}deg`);
    });
}

event_stream = new ReconnectingEventSource('event-stream/');

event_stream.addEventListener('message', function (event) {
    setGaugeClusterData(event.data);
}, false);