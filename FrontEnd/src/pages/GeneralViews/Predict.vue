<template>

  <div class="row">
    <div style="text-align: center" class="col-md-12">
      <img src="@/assets/imgs/documents.png" width="200px"/>
      <h2 style="text-align: center; color: #16a085">Predict Mohammedia Weather</h2>
    </div>
    <div style="text-align: center" class="col-md-1"></div>

    <div style="text-align: center" class="col-md-3">
      <div class="card"
           style="background-image: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)), url('../../assets/images/night.jpg');">
        <div class="card-header">
          <h2 style="text-align: center">Today</h2>
          <select v-model="todayHour" class="form-control" style="background-color: white"
                  @change="onTodayHourUpdated($event)">
            <option v-for="option in options" :value="option">
              {{ option }}
            </option>
          </select>
          <img src="@/assets/imgs/sun.png" width="140px"/>
          <h3 style="text-align: center; color: teal">Forecast : {{ todayWeather }}</h3>
        </div>
        <div class="card-body">
          <h4 style="text-align: center; margin-top: -28px">Humidity : {{ this.todayHumidity }} %<br>
            Temperature : {{ this.todayTemperature }} °C<br>
            Wind Speed : {{ this.todayWindSpeed }} m/s</h4>
        </div>
      </div>
    </div>

    <div style="text-align: center" class="col-md-3">
      <div class="card"
           style="background-image: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)), url('../../assets/images/night.jpg');">
        <div class="card-header">
          <h2 style="text-align: center">Tomorrow</h2>
          <select v-model="tomorrowHour" class="form-control" style="background-color: white"
                  @change="onTomorrowHourUpdated($event)">
            <option v-for="option in options" :value="option">
              {{ option }}
            </option>
          </select>
          <img src="@/assets/imgs/sun.png" width="140px"/>
          <h3 style="text-align: center; color: teal">Forecast : {{ tomorrowWeather }}</h3>
        </div>
        <div class="card-body">
          <h4 style="text-align: center; margin-top: -28px">Humidity : {{ this.tomorrowHumidity }} %<br>
            Temperature : {{ this.tomorrowTemperature }} °C<br>
            Wind Speed : {{ this.tomorrowWindSpeed }} m/s</h4>
        </div>
      </div>
    </div>

    <div style="text-align: center" class="col-md-3">
      <div class="card"
           style="background-image: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)), url('../../assets/images/night.jpg');">
        <div class="card-header">
          <h2 style="text-align: center">After Tomorrow</h2>
          <select v-model="afterTomorrowHour" class="form-control" style="background-color: white"
                  @change="onAfterTomorrowHourUpdated($event)">
            <option v-for="option in options" :value="option">
              {{ option }}
            </option>
          </select>
          <img src="@/assets/imgs/sun.png" width="140px"/>
          <h3 style="text-align: center; color: teal">Forecast : {{ afterTomorrowWeather }}</h3>
        </div>
        <div class="card-body">
          <h4 style="text-align: center; margin-top: -28px">Humidity : {{ this.afterTomorrowHumidity }} %<br>
            Temperature : {{ this.afterTomorrowTemperature }} °C<br>
            Wind Speed : {{ this.afterTomorrowWindSpeed }} m/s</h4>
        </div>
      </div>
    </div>


    <div style="text-align: center" class="col-md-1"></div>
    <div style="text-align: center" class="col-md-12"></div>
    <div style="text-align: center" class="col-md-4"></div>
    <div style="text-align: center" class="col-md-4">
      <div class="card"
           style="background-image: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)), url('../../assets/images/night.jpg');">
        <div class="card-header">
          <h2 style="text-align: center">Another Date (2023)</h2>
          <div class="row">
            <div style="text-align: center" class="col-md-4">
              <select v-model="selectedHour" class="form-control" style="background-color: white">
                <option v-for="option in options" :value="option">
                  {{ option }}
                </option>
              </select>
            </div>
            <div style="text-align: center" class="col-md-4">
              <select v-model="selectedDate" class="form-control" style="background-color: white">
                <option v-for="option in days" :value="option">
                  {{ option }}
                </option>
              </select>
            </div>
            <div style="text-align: center" class="col-md-4">
              <select v-model="selectedMonth" class="form-control" style="background-color: white">
                <option v-for="option in months" :value="option">
                  {{ option }}
                </option>
              </select>
            </div>
            <div style="text-align: center" class="col-md-12">
              <div style="text-align: center" class="my-12">
                <n-button
                    type="button"
                    class="btn btn-round btn-google"
                    @click.native="predictAnother()">
                  Predict
                </n-button>
              </div>
            </div>
          </div>
          <img src="@/assets/imgs/sun.png" width="140px"/>
          <h3 style="text-align: center; color: teal">Forecast : {{ selectedDateWeather }}</h3>
        </div>
        <div class="card-body">
          <h4 style="text-align: center; margin-top: -28px">Humidity : {{ this.selectedDateHumidity }} %<br>
            Temperature : {{ this.selectedDateTemperature }} °C<br>
            Wind Speed : {{ this.selectedDateWindSpeed }} m/s</h4>
        </div>
      </div>
    </div>
    <div style="text-align: center" class="col-md-4"></div>
  </div>


</template>
<script>
import {Table, TableColumn} from 'element-ui';
import axios from "axios";
import Vue from 'vue'
import VueCookies from 'vue-cookies'

Vue.use(VueCookies)

export default {
  created() {
  },
  mounted() {
    let date = new Date();
    let hour = date.getHours();
    let day = date.getDate();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();
    if (hour < 10) {
      hour = '0' + hour;
    }
    hour += ':00';
    this.todayHour = hour;
    let first = hour.split(":")[0];
    if (first.startsWith("0")) {
      first = first.substring(1);
    }
    hour = first;
    this.getHumidityPrediction(hour, day, month, year);
    this.getTemperaturePrediction(hour, day, month, year);
    this.getWeatherPrediction(hour, day, month, year);
    this.getWindSpeedPrediction(hour, day, month, year);

    this.getHumidityPrediction('8', day + 1, month, year);
    this.getTemperaturePrediction('8', day + 1, month, year);
    this.getWeatherPrediction('8', day + 1, month, year);
    this.getWindSpeedPrediction('8', day + 1, month, year);

    this.getHumidityPrediction('8', day + 2, month, year);
    this.getTemperaturePrediction('8', day + 2, month, year);
    this.getWeatherPrediction('8', day + 2, month, year);
    this.getWindSpeedPrediction('8', day + 2, month, year);
  },
  components: {
    [Table.name]: Table,
    [TableColumn.name]: TableColumn
  },
  data() {
    return {
      options: ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
      days: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
      months: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],

      selectedHour: '00:00',
      selectedDate: '01',
      selectedMonth: 'January',

      todayHour: '00:00',
      todayWeather: '',
      todayHumidity: 0,
      todayTemperature: 0,
      todayWindSpeed: 0,

      tomorrowHour: '00:00',
      tomorrowWeather: '',
      tomorrowHumidity: 0,
      tomorrowTemperature: 0,
      tomorrowWindSpeed: 0,

      afterTomorrowHour: '00:00',
      afterTomorrowWeather: '',
      afterTomorrowHumidity: 0,
      afterTomorrowTemperature: 0,
      afterTomorrowWindSpeed: 0,

      selectedDateHour: '00:00',
      selectedDateWeather: '',
      selectedDateHumidity: 0,
      selectedDateTemperature: 0,
      selectedDateWindSpeed: 0,
    };
  },
  methods: {
    onTodayHourUpdated(event) {
      let first = event.target.value.toString().split(":")[0];
      if (first.startsWith("0")) {
        first = first.substring(1);
      }
      console.log(first);
      let hour = first
      let date = new Date();
      let day = date.getDate();
      let month = date.getMonth() + 1;
      let year = date.getFullYear();
      this.getHumidityPrediction(hour, day, month, year);
    },
    onTomorrowHourUpdated(event) {
      let first = event.target.value.toString().split(":")[0];
      if (first.startsWith("0")) {
        first = first.substring(1);
      }
      console.log(first);
      let hour = first
      let date = new Date();
      let day = date.getDate() + 1;
      let month = date.getMonth() + 1;
      let year = date.getFullYear();
      this.getHumidityPrediction(hour, day, month, year);
    },
    onAfterTomorrowHourUpdated(event) {
      let first = event.target.value.toString().split(":")[0];
      if (first.startsWith("0")) {
        first = first.substring(1);
      }
      console.log(first);
      let hour = first
      let date = new Date();
      let day = date.getDate() + 2;
      let month = date.getMonth() + 1;
      let year = date.getFullYear();
      this.getHumidityPrediction(hour, day, month, year);
    },
    async predictAnother() {
      let first = this.selectedHour.toString().split(":")[0];
      if (first.startsWith("0")) {
        first = first.substring(1);
      }
      let hour = first
      first = this.selectedDate.toString();
      if (first.startsWith("0")) {
        first = first.substring(1);
      }
      let date = new Date();
      let day = first;
      let month = '';
      switch (this.selectedMonth) {
        case 'January':
          month = '1';
          break;
        case 'February':
          month = '2';
          break;
        case 'March':
          month = '3';
          break;
        case 'April':
          month = '4';
          break;
        case 'May':
          month = '5';
          break;
        case 'June':
          month = '6';
          break;
        case 'July':
          month = '7';
          break;
        case 'August':
          month = '8';
          break;
        case 'September':
          month = '9';
          break;
        case 'October':
          month = '10';
          break;
        case 'November':
          month = '11';
          break;
        case 'December':
          month = '12';
          break;
      }
      let year = date.getFullYear();
      this.getHumidityPrediction(hour, day, month, year);
      this.getTemperaturePrediction(hour, day, month, year);
      this.getWeatherPrediction(hour, day, month, year);
      this.getWindSpeedPrediction(hour, day, month, year);
    },
  async getHumidityPrediction(hour, day, month, year) {
    axios.get("http://localhost:8000/predict/humidity/" + hour + "/" + day + "/" + month + "/" + year)
        .then(response => {
          if (day === new Date().getDate()) {
            this.todayHumidity = response.data.value.toFixed(2);
          } else if (day === new Date().getDate() + 1) {
            this.tomorrowHumidity = response.data.value.toFixed(2);
          } else if (day === new Date().getDate() + 2) {
            this.afterTomorrowHumidity = response.data.value.toFixed(2);
          } else {
            this.selectedDateHumidity = response.data.value.toFixed(2);
          }
        })
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
  },
  async getWindSpeedPrediction(hour, day, month, year) {
    axios.get("http://localhost:8000/predict/wind/" + hour + "/" + day + "/" + month + "/" + year)
        .then(response => {
          if (day === new Date().getDate()) {
            this.todayWindSpeed = response.data.value.toFixed(2);
          } else if (day === new Date().getDate() + 1) {
            this.tomorrowWindSpeed = response.data.value.toFixed(2);
          } else if (day === new Date().getDate() + 2) {
            this.afterTomorrowWindSpeed = response.data.value.toFixed(2);
          } else {
            this.selectedDateWindSpeed = response.data.value.toFixed(2);
          }
        })
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
  },
  async getTemperaturePrediction(hour, day, month, year) {
    axios.get("http://localhost:8000/predict/temperature/" + hour + "/" + day + "/" + month + "/" + year)
        .then(response => {
          if (day === new Date().getDate()) {
            this.todayTemperature = response.data.value.toFixed(2);
          } else if (day === new Date().getDate() + 1) {
            this.tomorrowTemperature = response.data.value.toFixed(2);
          } else if (day === new Date().getDate() + 2) {
            this.afterTomorrowTemperature = response.data.value.toFixed(2);
          } else {
            this.selectedDateTemperature = response.data.value.toFixed(2);
          }
        })
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
  },
  async getWeatherPrediction(hour, day, month, year) {
    axios.get("http://localhost:8000/predict/weather/" + hour + "/" + day + "/" + month + "/" + year)
        .then(response => {
          if (day === new Date().getDate()) {
            this.todayWeather = response.data.weather;
          } else if (day === new Date().getDate() + 1) {
            this.tomorrowWeather = response.data.weather;
          } else if (day === new Date().getDate() + 2) {
            this.afterTomorrowWeather = response.data.weather;
          } else {
            this.selectedDateWeather = response.data.weather;
          }
        })
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
  }
  },
}
</script>
<style>
section {
  width: 100%;
  padding-top: 25px;

  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

.cloudiness img {
  width: 48px;
  height: 48px;
  vertical-align: middle;
}

.wind-speed img {
  width: 48px;
  height: 48px;
  vertical-align: middle;
}

.humidity img {
  width: 48px;
  height: 48px;
  vertical-align: middle;
}

.temperature__value {
  font-size: 7em;
  color: rgba(255, 255, 255, 0.75);
}

.temperature__right {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.temperature__scale {
  padding-top: 5px;
  font-size: 2em;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.75);
}

.temperature__high {
  padding-top: 5px;
}

.temperature__high img {
  vertical-align: middle;
}

.temperature__low img {
  vertical-align: middle;
}
</style>
