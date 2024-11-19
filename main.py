import threading
from earth import Earth
from satellite import Satellite

def main():
    earth = Earth()
    satellite = Satellite()

    earth_thread = threading.Thread(target=earth.send_data)
    satellite_thread = threading.Thread(target=satellite.receive_data)

    earth_thread.start()
    satellite_thread.start()

    earth_thread.join()
    satellite_thread.join()

if __name__ == "__main__":
    main()
