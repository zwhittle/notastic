import Controller from '@ember/controller';
import { computed } from '@ember/object';

export default Controller.extend({

  form: computed(function() {
    const model = this.get('model');
    return {
      name: model.get('name')
    }
  })
});
