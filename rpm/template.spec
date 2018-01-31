Name:           ros-kinetic-rqt-reconfigure
Version:        0.4.9
Release:        0%{?dist}
Summary:        ROS rqt_reconfigure package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_reconfigure
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-python-qt-binding >= 0.2.19
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-console
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
Requires:       ros-kinetic-rqt-py-common
BuildRequires:  ros-kinetic-catkin

%description
This rqt plugin succeeds former dynamic_reconfigure's GUI (reconfigure_gui), and
provides the way to view and edit the parameters that are accessible via
dynamic_reconfigure. (12/27/2012) In the future, arbitrary parameters that are
not associated with any nodes (which are not handled by dynamic_reconfigure)
might become handled. However, currently as the name indicates, this pkg solely
is dependent on dynamic_reconfigure that allows access to only those params
latched to nodes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jan 30 2018 Scott K Logan <logans@cottsay.net> - 0.4.9-0
- Autogenerated by Bloom

* Fri Apr 28 2017 Scott K Logan <logans@cottsay.net> - 0.4.8-0
- Autogenerated by Bloom

