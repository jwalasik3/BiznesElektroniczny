// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

// IWYU pragma: private, include "DTrackInterface.h"
#include "UObject/ObjectMacros.h"
#include "UObject/ScriptMacros.h"

PRAGMA_DISABLE_DEPRECATION_WARNINGS
#ifdef DTRACKPLUGIN_DTrackInterface_generated_h
#error "DTrackInterface.generated.h already included, missing '#pragma once' in DTrackInterface.h"
#endif
#define DTRACKPLUGIN_DTrackInterface_generated_h

#define FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackInterface_h_71_GENERATED_BODY \
	friend struct Z_Construct_UScriptStruct_FDTrackFinger_Statics; \
	DTRACKPLUGIN_API static class UScriptStruct* StaticStruct();


template<> DTRACKPLUGIN_API UScriptStruct* StaticStruct<struct FDTrackFinger>();

#undef CURRENT_FILE_ID
#define CURRENT_FILE_ID FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackInterface_h


#define FOREACH_ENUM_EDTRACKCOORDINATESYSTEMTYPE(op) \
	op(EDTrackCoordinateSystemType::CST_Normal) \
	op(EDTrackCoordinateSystemType::CST_Powerwall) \
	op(EDTrackCoordinateSystemType::CST_Unreal_Adapted) 

enum class EDTrackCoordinateSystemType : uint8;
template<> struct TIsUEnumClass<EDTrackCoordinateSystemType> { enum { Value = true }; };
template<> DTRACKPLUGIN_API UEnum* StaticEnum<EDTrackCoordinateSystemType>();

#define FOREACH_ENUM_EDTRACKFINGERTYPE(op) \
	op(EDTrackFingerType::FT_Thumb) \
	op(EDTrackFingerType::FT_Index) \
	op(EDTrackFingerType::FT_Middle) \
	op(EDTrackFingerType::FT_Ring) \
	op(EDTrackFingerType::FT_Pinky) 

enum class EDTrackFingerType : uint8;
template<> struct TIsUEnumClass<EDTrackFingerType> { enum { Value = true }; };
template<> DTRACKPLUGIN_API UEnum* StaticEnum<EDTrackFingerType>();

PRAGMA_ENABLE_DEPRECATION_WARNINGS
