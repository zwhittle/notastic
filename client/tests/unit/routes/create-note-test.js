import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | create-note', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:create-note');
    assert.ok(route);
  });
});
