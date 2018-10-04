import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),

  model(note) {
    return this.get('store').peekRecord('note', note.note_id);
  },

  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('confirmingDelete', false);
    this.controller.set('isEditing', false);
    this.controller.set('form.client', model.get('client'));
    this.controller.set('form.project', model.get('project'));
    this.controller.set('form.body', model.get('body'));
  },

  actions: {
    delete(note) {
      note.deleteRecord();
      note.save().then(() => {
        this.transitionTo('notes');
      });
    },

    update(note) {
      const form = this.controller.get('form');

      note.set('client', form.client);
      note.set('project', form.project);
      note.set('body', form.body);

      note.save().then(() => {
        this.controller.set('isEditing', false);
      });
    }
  }
});
