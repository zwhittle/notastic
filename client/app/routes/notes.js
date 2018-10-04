import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),

  model() {
    return [{
      project: 1,
      client: 1,
      body: "wow this is cool",
      owner: "zach"
    }]
  }
});
