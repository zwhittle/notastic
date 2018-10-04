import Controller from '@ember/controller';
import { computed } from '@ember/object';

export default Controller.extend({
  from: computed(function() {
    return {
      name: '',
    }
  })
});
