import Controller from '@ember/controller';
import { computed } from '@ember/object';

export default Controller.extend({
  form: computed(function() {
    return {
      project: '',
      client: '',
      body: '',
    }
  })
});
