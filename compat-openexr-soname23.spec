#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB02B1CDFA2F82257 (nick@ilm.com)
#
Name     : compat-openexr-soname23
Version  : 2.2.1
Release  : 10
URL      : http://download.savannah.nongnu.org/releases/openexr/openexr-2.2.1.tar.gz
Source0  : http://download.savannah.nongnu.org/releases/openexr/openexr-2.2.1.tar.gz
Source99 : http://download.savannah.nongnu.org/releases/openexr/openexr-2.2.1.tar.gz.sig
Summary  : OpenEXR image library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: compat-openexr-soname23-bin = %{version}-%{release}
Requires: compat-openexr-soname23-lib = %{version}-%{release}
Requires: compat-openexr-soname23-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : fltk-dev
BuildRequires : ilmbase-dev
BuildRequires : zlib-dev
Patch1: build.patch

%description
ABOUT THE OPENEXR LIBRARIES
----------------------------
IlmImf is our "EXR" file format for storing 16-bit FP images.  Libraries in
this package depend on the IlmBase library.

%package bin
Summary: bin components for the compat-openexr-soname23 package.
Group: Binaries
Requires: compat-openexr-soname23-license = %{version}-%{release}

%description bin
bin components for the compat-openexr-soname23 package.


%package dev
Summary: dev components for the compat-openexr-soname23 package.
Group: Development
Requires: compat-openexr-soname23-lib = %{version}-%{release}
Requires: compat-openexr-soname23-bin = %{version}-%{release}
Provides: compat-openexr-soname23-devel = %{version}-%{release}

%description dev
dev components for the compat-openexr-soname23 package.


%package doc
Summary: doc components for the compat-openexr-soname23 package.
Group: Documentation

%description doc
doc components for the compat-openexr-soname23 package.


%package lib
Summary: lib components for the compat-openexr-soname23 package.
Group: Libraries
Requires: compat-openexr-soname23-license = %{version}-%{release}

%description lib
lib components for the compat-openexr-soname23 package.


%package license
Summary: license components for the compat-openexr-soname23 package.
Group: Default

%description license
license components for the compat-openexr-soname23 package.


%prep
%setup -q -n openexr-2.2.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549594041
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -std=gnu++98"
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1549594041
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-openexr-soname23
cp COPYING %{buildroot}/usr/share/package-licenses/compat-openexr-soname23/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/compat-openexr-soname23/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/exrenvmap
%exclude /usr/bin/exrheader
%exclude /usr/bin/exrmakepreview
%exclude /usr/bin/exrmaketiled
%exclude /usr/bin/exrmultipart
%exclude /usr/bin/exrmultiview
%exclude /usr/bin/exrstdattr

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/OpenEXR/ImfAcesFile.h
%exclude /usr/include/OpenEXR/ImfArray.h
%exclude /usr/include/OpenEXR/ImfAttribute.h
%exclude /usr/include/OpenEXR/ImfB44Compressor.h
%exclude /usr/include/OpenEXR/ImfBoxAttribute.h
%exclude /usr/include/OpenEXR/ImfCRgbaFile.h
%exclude /usr/include/OpenEXR/ImfChannelList.h
%exclude /usr/include/OpenEXR/ImfChannelListAttribute.h
%exclude /usr/include/OpenEXR/ImfChromaticities.h
%exclude /usr/include/OpenEXR/ImfChromaticitiesAttribute.h
%exclude /usr/include/OpenEXR/ImfCompositeDeepScanLine.h
%exclude /usr/include/OpenEXR/ImfCompression.h
%exclude /usr/include/OpenEXR/ImfCompressionAttribute.h
%exclude /usr/include/OpenEXR/ImfConvert.h
%exclude /usr/include/OpenEXR/ImfDeepCompositing.h
%exclude /usr/include/OpenEXR/ImfDeepFrameBuffer.h
%exclude /usr/include/OpenEXR/ImfDeepImageState.h
%exclude /usr/include/OpenEXR/ImfDeepImageStateAttribute.h
%exclude /usr/include/OpenEXR/ImfDeepScanLineInputFile.h
%exclude /usr/include/OpenEXR/ImfDeepScanLineInputPart.h
%exclude /usr/include/OpenEXR/ImfDeepScanLineOutputFile.h
%exclude /usr/include/OpenEXR/ImfDeepScanLineOutputPart.h
%exclude /usr/include/OpenEXR/ImfDeepTiledInputFile.h
%exclude /usr/include/OpenEXR/ImfDeepTiledInputPart.h
%exclude /usr/include/OpenEXR/ImfDeepTiledOutputFile.h
%exclude /usr/include/OpenEXR/ImfDeepTiledOutputPart.h
%exclude /usr/include/OpenEXR/ImfDoubleAttribute.h
%exclude /usr/include/OpenEXR/ImfEnvmap.h
%exclude /usr/include/OpenEXR/ImfEnvmapAttribute.h
%exclude /usr/include/OpenEXR/ImfExport.h
%exclude /usr/include/OpenEXR/ImfFloatAttribute.h
%exclude /usr/include/OpenEXR/ImfForward.h
%exclude /usr/include/OpenEXR/ImfFrameBuffer.h
%exclude /usr/include/OpenEXR/ImfFramesPerSecond.h
%exclude /usr/include/OpenEXR/ImfGenericInputFile.h
%exclude /usr/include/OpenEXR/ImfGenericOutputFile.h
%exclude /usr/include/OpenEXR/ImfHeader.h
%exclude /usr/include/OpenEXR/ImfHuf.h
%exclude /usr/include/OpenEXR/ImfIO.h
%exclude /usr/include/OpenEXR/ImfInputFile.h
%exclude /usr/include/OpenEXR/ImfInputPart.h
%exclude /usr/include/OpenEXR/ImfInt64.h
%exclude /usr/include/OpenEXR/ImfIntAttribute.h
%exclude /usr/include/OpenEXR/ImfKeyCode.h
%exclude /usr/include/OpenEXR/ImfKeyCodeAttribute.h
%exclude /usr/include/OpenEXR/ImfLineOrder.h
%exclude /usr/include/OpenEXR/ImfLineOrderAttribute.h
%exclude /usr/include/OpenEXR/ImfLut.h
%exclude /usr/include/OpenEXR/ImfMatrixAttribute.h
%exclude /usr/include/OpenEXR/ImfMisc.h
%exclude /usr/include/OpenEXR/ImfMultiPartInputFile.h
%exclude /usr/include/OpenEXR/ImfMultiPartOutputFile.h
%exclude /usr/include/OpenEXR/ImfMultiView.h
%exclude /usr/include/OpenEXR/ImfName.h
%exclude /usr/include/OpenEXR/ImfNamespace.h
%exclude /usr/include/OpenEXR/ImfOpaqueAttribute.h
%exclude /usr/include/OpenEXR/ImfOutputFile.h
%exclude /usr/include/OpenEXR/ImfOutputPart.h
%exclude /usr/include/OpenEXR/ImfPartHelper.h
%exclude /usr/include/OpenEXR/ImfPartType.h
%exclude /usr/include/OpenEXR/ImfPixelType.h
%exclude /usr/include/OpenEXR/ImfPreviewImage.h
%exclude /usr/include/OpenEXR/ImfPreviewImageAttribute.h
%exclude /usr/include/OpenEXR/ImfRational.h
%exclude /usr/include/OpenEXR/ImfRationalAttribute.h
%exclude /usr/include/OpenEXR/ImfRgba.h
%exclude /usr/include/OpenEXR/ImfRgbaFile.h
%exclude /usr/include/OpenEXR/ImfRgbaYca.h
%exclude /usr/include/OpenEXR/ImfStandardAttributes.h
%exclude /usr/include/OpenEXR/ImfStringAttribute.h
%exclude /usr/include/OpenEXR/ImfStringVectorAttribute.h
%exclude /usr/include/OpenEXR/ImfTestFile.h
%exclude /usr/include/OpenEXR/ImfThreading.h
%exclude /usr/include/OpenEXR/ImfTileDescription.h
%exclude /usr/include/OpenEXR/ImfTileDescriptionAttribute.h
%exclude /usr/include/OpenEXR/ImfTiledInputFile.h
%exclude /usr/include/OpenEXR/ImfTiledInputPart.h
%exclude /usr/include/OpenEXR/ImfTiledOutputFile.h
%exclude /usr/include/OpenEXR/ImfTiledOutputPart.h
%exclude /usr/include/OpenEXR/ImfTiledRgbaFile.h
%exclude /usr/include/OpenEXR/ImfTimeCode.h
%exclude /usr/include/OpenEXR/ImfTimeCodeAttribute.h
%exclude /usr/include/OpenEXR/ImfVecAttribute.h
%exclude /usr/include/OpenEXR/ImfVersion.h
%exclude /usr/include/OpenEXR/ImfWav.h
%exclude /usr/include/OpenEXR/ImfXdr.h
%exclude /usr/include/OpenEXR/OpenEXRConfig.h
%exclude /usr/lib64/libIlmImf.so
%exclude /usr/lib64/libIlmImfUtil.so
%exclude /usr/lib64/pkgconfig/OpenEXR.pc
%exclude /usr/share/aclocal/openexr.m4

%files doc
%defattr(0644,root,root,0755)
%exclude /usr/share/doc/OpenEXR-2.2.1/InterpretingDeepPixels.pdf
%exclude /usr/share/doc/OpenEXR-2.2.1/MultiViewOpenEXR.pdf
%exclude /usr/share/doc/OpenEXR-2.2.1/OpenEXRFileLayout.pdf
%exclude /usr/share/doc/OpenEXR-2.2.1/ReadingAndWritingImageFiles.pdf
%exclude /usr/share/doc/OpenEXR-2.2.1/TechnicalIntroduction.pdf
%exclude /usr/share/doc/OpenEXR-2.2.1/TheoryDeepPixels.pdf
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/drawImage.cpp
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/drawImage.h
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/generalInterfaceExamples.cpp
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/generalInterfaceExamples.h
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/generalInterfaceTiledExamples.cpp
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/generalInterfaceTiledExamples.h
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/lowLevelIoExamples.cpp
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/lowLevelIoExamples.h
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/main.cpp
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/namespaceAlias.h
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/previewImageExamples.cpp
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/previewImageExamples.h
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/rgbaInterfaceExamples.cpp
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/rgbaInterfaceExamples.h
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/rgbaInterfaceTiledExamples.cpp
%exclude /usr/share/doc/OpenEXR-2.2.1/examples/rgbaInterfaceTiledExamples.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/libIlmImf-2_2.so.23
/usr/lib64/libIlmImf-2_2.so.23.0.0
/usr/lib64/libIlmImfUtil-2_2.so.23
/usr/lib64/libIlmImfUtil-2_2.so.23.0.0

%files license
%defattr(0644,root,root,0755)
%exclude /usr/share/package-licenses/compat-openexr-soname23/COPYING
%exclude /usr/share/package-licenses/compat-openexr-soname23/LICENSE
