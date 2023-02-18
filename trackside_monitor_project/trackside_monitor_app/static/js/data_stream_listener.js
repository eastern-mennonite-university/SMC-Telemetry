const GAUGE_BOUNDS = {
    'rpm': [0, 5000],
    'speed': [0, 50],
    'voltage': [10, 18],
    'o2s': [0, 1], // Set to [0, 1] until realistic bound is known
    'econ': [0, 1], // Set to [0, 1] until realistic bound is known
    'temp-air': [0, 150],
};

const MAX_MEASURES = {
    'rpm': 225,
    'speed': 225,
    'voltage': 180,
    'o2s': 164,
    'econ': 164,
    'temp-air': 180,
};

const GAUGE_UNITS = {
    'rpm': 'deg',
    'speed': 'deg',
    'voltage': 'deg',
    'o2s': 'px',
    'econ': 'px',
    'temp-air': 'deg',
}

function setGaugeClusterData(data) {
    Object.entries(JSON.parse(data)).forEach(entry => {
        const [key, value] = entry;
        let unit = GAUGE_UNITS[key];
        let mapping_slope = MAX_MEASURES[key] / (GAUGE_BOUNDS[key][1] - GAUGE_BOUNDS[key][0]);
        let measure = mapping_slope * value - GAUGE_BOUNDS[key][0] * mapping_slope;
        document.getElementById(`${key}-gauge`).style.setProperty('--gauge-measure', `${measure}${unit}`);
    });
}

event_stream = new ReconnectingEventSource('event-stream/');

event_stream.addEventListener('message', function (event) {
    setGaugeClusterData(event.data);
}, false);