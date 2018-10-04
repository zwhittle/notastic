import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),

  model(project) {
    return this.get('store').peekRecord('project', project.project_id);
  },

  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('confirmingDelete', false);
    this.controller.set('isEditing', false);
    this.controller.set('form.name', model.get('name'));
  },

  actions: {
    delete(project) {
      project.deleteRecord();
      project.save().then(() => {
        this.transitionTo('projects');
      });
    },

    update(project) {
      const form = this.controller.get('form');

      project.set('name', form.name);

      project.save().then(() => {
        this.controller.set('isEditing', false);
      });
    }
  }
});
