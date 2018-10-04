import Controller from '@ember/controller';
import { computed } from '@ember/object';

export default Controller.extend({

  form: computed(function() {
    const model = this.get('model');
    return {
      client: model.get('title'),
      project: model.get('project'),
      body: model.get('body')
    }
  })
});
