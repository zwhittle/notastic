import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),

  model() {
    // return [{
    //   name: "Umberella Corporation",
    //   owner: "zach"
    // }]
    return this.get('store').findAll('client');
  }
});
