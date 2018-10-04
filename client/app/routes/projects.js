import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),

  model() {
    // return [
    //   {
    //     name: 'Theseus',
    //     client: {
    //       name: 'Umbrella Corporation',
    //       owner: 'zach'
    //     },
    //     owner: 'zach',
    //     status: {
    //       "name": "Green",
    //       "color_code": "#32c832",
    //       "red": 50,
    //       "green": 200,
    //       "blue": 50
    //     },
    //     project_phase: {
    //       name: "Pre-Sale"
    //     },
    //     go_live_date: "01/01/2019"
    //   }
    // ]
    return this.get('store').findAll('project');
  }
});
