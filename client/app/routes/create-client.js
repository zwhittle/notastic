import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),

  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('form.name', '');
  },

  actions: {
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');

      const newClient = store.createRecord('client', {
        name: form.name,
      });

      newClient.save().then(() => {
        this.transitionTo('clients');
      });
    },

    cancel() {
      this.transitionTo('clients');
    }
  }
});
