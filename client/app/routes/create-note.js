import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),

  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('form.client', '');
    this.controller.set('form.project', '');
    this.controller.set('form.body', '');
  },

  actions: {
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');

      const newNote = store.createRecord('note', {
        client: form.client,
        project: form.project,
        body: form.body,
      });

      newNote.save().then(() => {
        this.transitionTo('notes');
      });
    },

    cancel() {
      this.transitionTo('notes');
    }
  }
});
