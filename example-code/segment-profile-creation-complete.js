let Analytics = require('analytics-node');
let analytics = new Analytics(process.env.SEGMENT_WRITE_KEY, { flushAt: 1 });
analytics.identify({
    userId: process.env.SEGMENT_USER,
    traits: {
      name: 'Superclass 2022',
      email: 'replaceme@example.com',
      plan: 'Premium',
      friends: 1
    }
  });
