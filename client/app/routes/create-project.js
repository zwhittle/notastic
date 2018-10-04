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

      const newProject = store.createRecord('project', {
        name: form.name,
      });

      newProject.save().then(() => {
        this.transitionTo('projects');
      });
    },

    cancel() {
      this.transitionTo('projects');
    }
  }
});
