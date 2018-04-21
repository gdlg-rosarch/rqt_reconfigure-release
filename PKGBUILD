# Script generated with Bloom
pkgdesc="ROS - This rqt plugin succeeds former dynamic_reconfigure's GUI (reconfigure_gui), and provides the way to view and edit the parameters that are accessible via dynamic_reconfigure.<br/> <br/> (12/27/2012) In the future, arbitrary parameters that are not associated with any nodes (which are not handled by dynamic_reconfigure) might become handled. However, currently as the name indicates, this pkg solely is dependent on dynamic_reconfigure that allows access to only those params latched to nodes."
url='http://wiki.ros.org/rqt_reconfigure'

pkgname='ros-kinetic-rqt-reconfigure'
pkgver='0.4.9_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-dynamic-reconfigure'
'ros-kinetic-python-qt-binding>=0.2.19'
'ros-kinetic-rospy'
'ros-kinetic-rqt-console'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-rqt-py-common'
)

conflicts=()
replaces=()

_dir=rqt_reconfigure
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_reconfigure $srcdir/rqt_reconfigure
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

