import moment from 'moment';

export default {
    install: (app, options) => {
        app.config.globalProperties.$moment = (param) => {
            return moment(param)
        }
    }
}