import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),

  model(client) {
    return this.get('store').peekRecord('client', client.client_id);
  },

  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('confirmingDelete', false);
    this.controller.set('isEditing', false);
    this.controller.set('form.name', model.get('name'));
  },

  actions: {
    delete(client) {
      client.deleteRecord();
      client.save().then(() => {
        this.transitionTo('clients');
      });
    },

    update(client) {
      const form = this.controller.get('form');

      client.set('name', form.name);

      client.save().then(() => {
        this.controller.set('isEditing', false);
      });
    }
  }
});
